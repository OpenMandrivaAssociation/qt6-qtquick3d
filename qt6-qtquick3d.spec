#define beta rc2
#define snapshot 20200627
%define major 6

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtquick3d
Version:	6.0.1
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtquick3d-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtquick3d-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{major} Quick 3D
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	%{_lib}Qt%{major}Core-devel
BuildRequires:	%{_lib}Qt%{major}Gui-devel
BuildRequires:	%{_lib}Qt%{major}Network-devel
BuildRequires:	%{_lib}Qt%{major}Qml-devel
BuildRequires:	%{_lib}Qt%{major}QmlDevTools-devel
BuildRequires:	%{_lib}Qt%{major}QmlModels-devel
BuildRequires:	%{_lib}Qt%{major}QmlQuick-devel
BuildRequires:	%{_lib}Qt%{major}QmlQuickWidgets-devel
BuildRequires:	%{_lib}Qt%{major}Xml-devel
BuildRequires:	%{_lib}Qt%{major}Widgets-devel
BuildRequires:	%{_lib}Qt%{major}QmlDevTools-devel
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}PrintSupport-devel
BuildRequires:	%{_lib}Qt%{major}OpenGL-devel
BuildRequires:	%{_lib}Qt%{major}OpenGLWidgets-devel
BuildRequires:	%{_lib}Qt%{major}DBus-devel
BuildRequires:	qt%{major}-cmake
BuildRequires:	qt%{major}-qtdeclarative
BuildRequires:	qt%{major}-qtshadertools >= %{version}-0
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

%prep
%autosetup -p1 -n qtquick3d%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
# FIXME why are OpenGL lib paths autodetected incorrectly, preferring
# /usr/lib over /usr/lib64 even on 64-bit boxes?
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_install -C build
# Static helper lib without headers -- useless
rm -f %{buildroot}%{_libdir}/qt6/%{_lib}/libpnp_basictools.a
# Put stuff where tools will find it
# We can't do the same for %{_includedir} right now because that would
# clash with qt5 (both would want to have /usr/include/QtCore and friends)
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir}/cmake
for i in %{buildroot}%{_qtdir}/lib/*.so*; do
	ln -s qt%{major}/lib/$(basename ${i}) %{buildroot}%{_libdir}/
done
for i in %{buildroot}%{_qtdir}/lib/cmake/*; do
	[ "$(basename ${i})" = "Qt6BuildInternals" -o "$(basename ${i})" = "Qt6Qml" ] && continue
	ln -s ../qt%{major}/lib/cmake/$(basename ${i}) %{buildroot}%{_libdir}/cmake/
done

%files
%{_libdir}/cmake/Qt6Quick3D
%{_libdir}/cmake/Qt6Quick3DAssetImport
%{_libdir}/cmake/Qt6Quick3DRuntimeRender
%{_libdir}/cmake/Qt6Quick3DTools
%{_libdir}/cmake/Qt6Quick3DUtils
%{_libdir}/libQt6Quick3D.so
%{_libdir}/libQt6Quick3D.so.*
%{_libdir}/libQt6Quick3DAssetImport.so
%{_libdir}/libQt6Quick3DAssetImport.so.*
%{_libdir}/libQt6Quick3DRuntimeRender.so
%{_libdir}/libQt6Quick3DRuntimeRender.so.*
%{_libdir}/libQt6Quick3DUtils.so
%{_libdir}/libQt6Quick3DUtils.so.*
%{_qtdir}/bin/balsam
%{_qtdir}/bin/meshdebug
%{_qtdir}/bin/shadergen
%{_qtdir}/examples/quick3d
%{_qtdir}/include/QtQuick3D
%{_qtdir}/include/QtQuick3DAssetImport
%{_qtdir}/include/QtQuick3DRuntimeRender
%{_qtdir}/include/QtQuick3DUtils
%{_qtdir}/lib/cmake/Qt6BuildInternals/StandaloneTests/QtQuick3DTestsConfig.cmake
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qtdir}/lib/cmake/Qt6Quick3D
%{_qtdir}/lib/cmake/Qt6Quick3DAssetImport
%{_qtdir}/lib/cmake/Qt6Quick3DRuntimeRender
%{_qtdir}/lib/cmake/Qt6Quick3DTools
%{_qtdir}/lib/cmake/Qt6Quick3DUtils
%{_qtdir}/lib/libQt6Quick3D.prl
%{_qtdir}/lib/libQt6Quick3D.so
%{_qtdir}/lib/libQt6Quick3D.so.*
%{_qtdir}/lib/libQt6Quick3DAssetImport.prl
%{_qtdir}/lib/libQt6Quick3DAssetImport.so
%{_qtdir}/lib/libQt6Quick3DAssetImport.so.*
%{_qtdir}/lib/libQt6Quick3DRuntimeRender.prl
%{_qtdir}/lib/libQt6Quick3DRuntimeRender.so
%{_qtdir}/lib/libQt6Quick3DRuntimeRender.so.*
%{_qtdir}/lib/libQt6Quick3DUtils.prl
%{_qtdir}/lib/libQt6Quick3DUtils.so
%{_qtdir}/lib/libQt6Quick3DUtils.so.*
%{_qtdir}/lib/metatypes/*.json
%{_qtdir}/mkspecs/modules/*.pri
%{_qtdir}/modules/*.json
%{_qtdir}/plugins/assetimporters
%{_qtdir}/qml/QtQuick3D
