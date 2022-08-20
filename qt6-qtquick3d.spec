%define beta beta3
#define snapshot 20200627
%define major 6

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtquick3d
Version:	6.4.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtquick3d-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtquick3d-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Patch0:		qtquick3d-c++20.patch
Group:		System/Libraries
Summary:	Qt %{major} Quick 3D
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	%{_lib}Qt%{major}Core-devel
BuildRequires:	%{_lib}Qt%{major}Gui-devel
BuildRequires:	%{_lib}Qt%{major}Network-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6QmlLocalStorage)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6QmlWorkerScript)
BuildRequires:	cmake(Qt6QmlXmlListModel)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6QuickControls2Impl)
BuildRequires:	cmake(Qt6QuickDialogs2)
BuildRequires:	cmake(Qt6QuickDialogs2QuickImpl)
BuildRequires:	cmake(Qt6QuickDialogs2Utils)
BuildRequires:	cmake(Qt6QuickLayouts)
BuildRequires:	cmake(Qt6QuickTemplates2)
BuildRequires:	cmake(Qt6QuickTest)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6QuickTimeline)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	%{_lib}Qt%{major}Xml-devel
BuildRequires:	%{_lib}Qt%{major}Widgets-devel
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}PrintSupport-devel
BuildRequires:	%{_lib}Qt%{major}OpenGL-devel
BuildRequires:	%{_lib}Qt%{major}OpenGLWidgets-devel
BuildRequires:	%{_lib}Qt%{major}DBus-devel
BuildRequires:	qt%{major}-cmake
BuildRequires:	qt%{major}-qtdeclarative
BuildRequires:	cmake(Qt6ShaderTools) >= %{version}-0
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	cmake(LLVM)
BuildRequires:	cmake(Clang)
# Not really required, but referenced by LLVMExports.cmake
# (and then required because of the integrity check)
BuildRequires:	%{_lib}gpuruntime
License:	LGPLv3/GPLv3/GPLv2

%description
Qt %{major} Quick 3D

%define extra_devel_files_Quick3D \
%{_qtdir}/lib/cmake/Qt6/FindWrapBundledEmbreeConfigExtra.cmake \
%{_qtdir}/lib/cmake/Qt6BundledEmbree \
%{_qtdir}/lib/libQt6BundledEmbree.a

%qt6libs Quick3D Quick3DAssetImport Quick3DAssetUtils Quick3DEffects Quick3DHelpers Quick3DIblBaker Quick3DParticles Quick3DRuntimeRender Quick3DUtils Quick3DGlslParser Quick3DParticleEffects

%prep
%autosetup -p1 -n qtquick3d%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
# FIXME why are OpenGL lib paths autodetected incorrectly, preferring
# /usr/lib over /usr/lib64 even on 64-bit boxes?
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON \
	-DQT_MKSPECS_DIR:FILEPATH=%{_qtdir}/mkspecs

%build
#export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
#export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_install -C build

%files
%{_qtdir}/bin/balsam
%{_qtdir}/bin/balsamui
%{_qtdir}/bin/materialeditor
%{_qtdir}/bin/meshdebug
%{_qtdir}/bin/shadergen
%{_qtdir}/bin/shapegen
%{_qtdir}/bin/instancer
%{_qtdir}/examples/quick3d
%{_qtdir}/lib/cmake/Qt6/FindWrapQuick3DAssimp.cmake
%{_qtdir}/lib/cmake/Qt6BuildInternals/StandaloneTests/QtQuick3DTestsConfig.cmake
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qtdir}/lib/cmake/Qt6Quick3DTools
%{_qtdir}/lib/metatypes/*.json
%{_qtdir}/plugins/assetimporters
%{_qtdir}/qml/QtQuick3D
