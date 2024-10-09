#define beta rc2

Name:		qt6-qtquick3d
Version:	6.8.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qtquick3d-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtquick3d-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{qtmajor} 3D Library
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlCore)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6QmlLocalStorage)
BuildRequires:	cmake(Qt6QmlWorkerScript)
BuildRequires:	cmake(Qt6QmlXmlListModel)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6PacketProtocolPrivate)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6Quick)
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
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	qt6-qtdeclarative
BuildRequires:	cmake(Qt6ShaderTools) >= %{version}-0

BuildRequires:	qt6-cmake
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(OpenGL)
BuildRequires:	cmake(OpenXR)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
License:	LGPLv3/GPLv3/GPLv2

# How can this even compile upstream without the patch???
Patch100:	https://github.com/RenderKit/embree/commit/cda4cf1919bb2a748e78915fbd6e421a1056638d.patch

%description
Qt %{qtmajor} 3D library

%global extra_files_Quick3D \
%dir %{_qtdir}/qml/QtQuick3D \
%{_qtdir}/qml/QtQuick3D/Quick3D.qmltypes \
%{_qtdir}/qml/QtQuick3D/qmldir \
%{_qtdir}/qml/QtQuick3D/libqquick3dplugin.so \
%{_qtdir}/qml/QtQuick3D/designer \
%{_qtdir}/qml/QtQuick3D/MaterialEditor \
%{_qtdir}/bin/balsam \
%{_qtdir}/bin/balsamui \
%{_qtdir}/bin/instancer \
%{_qtdir}/bin/materialeditor \
%{_qtdir}/bin/meshdebug \
%{_qtdir}/bin/shadergen \
%{_qtdir}/bin/shapegen

%global extra_devel_files_Quick3D \
%{_qtdir}/lib/libQt6BundledEmbree.a \
%{_qtdir}/lib/cmake/Qt6BundledEmbree/Qt6BundledEmbree*.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qquick3dplugin*.cmake \
%{_qtdir}/lib/cmake/Qt6/FindWrapBundledEmbreeConfigExtra.cmake \
%{_qtdir}/lib/cmake/Qt6/FindWrapQuick3DAssimp.cmake

%global extra_devel_reqprov_Quick3D \
Requires: cmake(Qt%{qtmajor}Quick3DRuntimeRender)

%global extra_files_Quick3DAssetImport \
%dir %{_qtdir}/plugins/assetimporters \
%{_qtdir}/plugins/assetimporters/libassimp.so

%global extra_devel_files_Quick3DAssetImport \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dassetutilsplugin*.cmake

%global extra_files_Quick3DAssetUtils \
%dir %{_qtdir}/qml/QtQuick3D/AssetUtils \
%{_qtdir}/qml/QtQuick3D/AssetUtils/libqtquick3dassetutilsplugin.so \
%{_qtdir}/qml/QtQuick3D/AssetUtils/plugins.qmltypes \
%{_qtdir}/qml/QtQuick3D/AssetUtils/qmldir \
%{_qtdir}/qml/QtQuick3D/AssetUtils/designer

%global extra_files_Quick3DEffects \
%dir %{_qtdir}/qml/QtQuick3D/Effects \
%{_qtdir}/qml/QtQuick3D/Effects/*.qml \
%{_qtdir}/qml/QtQuick3D/Effects/libqtquick3deffectplugin.so \
%{_qtdir}/qml/QtQuick3D/Effects/qmldir \
%{_qtdir}/qml/QtQuick3D/Effects/Quick3DEffects.qmltypes \
%{_qtdir}/qml/QtQuick3D/Effects/designer

%global extra_devel_files_Quick3DEffects \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3deffectplugin*.cmake

%global extra_files_Quick3DHelpers \
%dir %{_qtdir}/qml/QtQuick3D/Helpers \
%{_qtdir}/qml/QtQuick3D/Helpers/libqtquick3dhelpersplugin.so \
%{_qtdir}/qml/QtQuick3D/Helpers/meshes/axisGrid.mesh \
%{_qtdir}/qml/QtQuick3D/Helpers/plugins.qmltypes \
%{_qtdir}/qml/QtQuick3D/Helpers/qmldir \
%{_qtdir}/qml/QtQuick3D/Helpers/*.qml \
%{_qtdir}/qml/QtQuick3D/Helpers/designer \
%{_qtdir}/qml/QtQuick3D/Helpers/impl

%global extra_devel_files_Quick3DHelpers \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dhelpersplugin*.cmake

%global extra_files_Quick3DParticleEffects \
%dir %{_qtdir}/qml/QtQuick3D/ParticleEffects \
%{_qtdir}/qml/QtQuick3D/ParticleEffects/qmldir \
%{_qtdir}/qml/QtQuick3D/ParticleEffects/Quick3DParticleEffects.qmltypes \
%{_qtdir}/qml/QtQuick3D/ParticleEffects/libqtquick3dparticleeffectsplugin.so \
%{_qtdir}/qml/QtQuick3D/ParticleEffects/designer

%global extra_devel_files_Quick3DParticleEffects \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dparticleeffectsplugin*.cmake

%global extra_files_Quick3DParticles \
%dir %{_qtdir}/qml/QtQuick3D/Particles3D \
%{_qtdir}/qml/QtQuick3D/Particles3D/qmldir \
%{_qtdir}/qml/QtQuick3D/Particles3D/plugins.qmltypes \
%{_qtdir}/qml/QtQuick3D/Particles3D/libqtquick3dparticles3dplugin.so \
%{_qtdir}/qml/QtQuick3D/Particles3D/designer

%global extra_devel_files_Quick3DParticles \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dparticles3dplugin*.cmake

%global extra_devel_reqprov_Quick3DRuntimeRender \
Requires: cmake(Qt%{qtmajor}Quick3DUtils)

%global extra_devel_files_Quick3DHelpersImpl \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtquick3dhelpersimplplugin*.cmake

%global extra_files_Quick3DXr \
%{_qtdir}/qml/QtQuick3D/Xr

%global extra_devel_files_Quick3DXr \
%{_qtdir}/lib/cmake/Qt6/FindWrapBundledOpenXRConfigExtra.cmake \
%{_qtdir}/lib/cmake/Qt6/FindWrapOpenXR.cmake \
%{_qtdir}/lib/cmake/Qt6/FindWrapSystemOpenXR.cmake \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6Quick3DXrplugin*

%package profiler
Summary: Profiler for QtQuick 3D
Group: Development/Tools

%description profiler
Profiler for QtQuick 3D

%files profiler
%{_qtdir}/lib/cmake/Qt6Qml/Qt6QQuick3DProfilerAdapter*
%{_qtdir}/plugins/qmltooling/libqmldbg_quick3dprofiler.so

%qt6libs Quick3D Quick3DAssetImport Quick3DAssetUtils Quick3DEffects Quick3DGlslParser Quick3DHelpers Quick3DIblBaker Quick3DParticleEffects Quick3DParticles Quick3DRuntimeRender Quick3DUtils Quick3DHelpersImpl Quick3DXr

%package examples
Summary:	Example code for the Qt 6 3D module
Group:		Documentation

%description examples
Example code for the Qt 6 3D module

%prep
%setup -q -n qtquick3d%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%autopatch -p1 -M 99
cd src/3rdparty/embree
%autopatch -p1 -m 100
cd -
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_MKSPECS_DIR:FILEPATH=%{_qtdir}/mkspecs \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall

%files examples
%{_qtdir}/examples
