#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xF442B36D614B06BC (reeves.87@gmail.com)
#
Name     : kdiff3
Version  : 1.10.7
Release  : 14
URL      : https://download.kde.org/stable/kdiff3/kdiff3-1.10.7.tar.xz
Source0  : https://download.kde.org/stable/kdiff3/kdiff3-1.10.7.tar.xz
Source1  : https://download.kde.org/stable/kdiff3/kdiff3-1.10.7.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 MIT
Requires: kdiff3-bin = %{version}-%{release}
Requires: kdiff3-data = %{version}-%{release}
Requires: kdiff3-lib = %{version}-%{release}
Requires: kdiff3-license = %{version}-%{release}
Requires: kdiff3-locales = %{version}-%{release}
Requires: kdiff3-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KDiff3-Readme
=============
Author: Joachim Eibl  (joachim.eibl at gmx.de)
Port to KF5/Qt5 by Michael Reeves (reeves.87@gmail.com)
KDiff3-Version: 1.10.6

%package bin
Summary: bin components for the kdiff3 package.
Group: Binaries
Requires: kdiff3-data = %{version}-%{release}
Requires: kdiff3-license = %{version}-%{release}

%description bin
bin components for the kdiff3 package.


%package data
Summary: data components for the kdiff3 package.
Group: Data

%description data
data components for the kdiff3 package.


%package doc
Summary: doc components for the kdiff3 package.
Group: Documentation
Requires: kdiff3-man = %{version}-%{release}

%description doc
doc components for the kdiff3 package.


%package lib
Summary: lib components for the kdiff3 package.
Group: Libraries
Requires: kdiff3-data = %{version}-%{release}
Requires: kdiff3-license = %{version}-%{release}

%description lib
lib components for the kdiff3 package.


%package license
Summary: license components for the kdiff3 package.
Group: Default

%description license
license components for the kdiff3 package.


%package locales
Summary: locales components for the kdiff3 package.
Group: Default

%description locales
locales components for the kdiff3 package.


%package man
Summary: man components for the kdiff3 package.
Group: Default

%description man
man components for the kdiff3 package.


%prep
%setup -q -n kdiff3-1.10.7
cd %{_builddir}/kdiff3-1.10.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703121290
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703121290
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdiff3
cp %{_builddir}/kdiff3-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kdiff3/47c547529aa3a83793060dc46dd05d2eb284de83 || :
cp %{_builddir}/kdiff3-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kdiff3/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kdiff3-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdiff3/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kdiff3-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdiff3/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kdiff3-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdiff3/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/kdiff3-%{version}/diff_ext_for_kdiff3/LICENSE %{buildroot}/usr/share/package-licenses/kdiff3/6c284580296aa36e06810ccb61e130fc422eb4d4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kdiff3
%find_lang diff_ext
%find_lang kdiff3fileitemactionplugin
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kdiff3
/usr/bin/kdiff3

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kdiff3.desktop
/usr/share/icons/hicolor/128x128/apps/kdiff3.png
/usr/share/icons/hicolor/16x16/apps/kdiff3.png
/usr/share/icons/hicolor/22x22/apps/kdiff3.png
/usr/share/icons/hicolor/256x256/apps/kdiff3.png
/usr/share/icons/hicolor/32x32/apps/kdiff3.png
/usr/share/icons/hicolor/48x48/apps/kdiff3.png
/usr/share/icons/hicolor/64x64/apps/kdiff3.png
/usr/share/icons/hicolor/scalable/apps/kdiff3.svgz
/usr/share/kservices5/kdiff3part.desktop
/usr/share/kxmlgui5/kdiff3/kdiff3_shell.rc
/usr/share/kxmlgui5/kdiff3part/kdiff3_part.rc
/usr/share/metainfo/org.kde.kdiff3.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kdiff3/index.cache.bz2
/usr/share/doc/HTML/ca/kdiff3/index.docbook
/usr/share/doc/HTML/ca/kdiff3/open_dialog.png
/usr/share/doc/HTML/de/kdiff3/index.cache.bz2
/usr/share/doc/HTML/de/kdiff3/index.docbook
/usr/share/doc/HTML/en/kdiff3/dirbrowser.png
/usr/share/doc/HTML/en/kdiff3/dirmergebig.png
/usr/share/doc/HTML/en/kdiff3/index.cache.bz2
/usr/share/doc/HTML/en/kdiff3/index.docbook
/usr/share/doc/HTML/en/kdiff3/iteminfo.png
/usr/share/doc/HTML/en/kdiff3/letter_by_letter.png
/usr/share/doc/HTML/en/kdiff3/merge_current.png
/usr/share/doc/HTML/en/kdiff3/new.png
/usr/share/doc/HTML/en/kdiff3/open_dialog.png
/usr/share/doc/HTML/en/kdiff3/screenshot_diff.png
/usr/share/doc/HTML/en/kdiff3/screenshot_merge.png
/usr/share/doc/HTML/en/kdiff3/triple_diff.png
/usr/share/doc/HTML/en/kdiff3/white_space.png
/usr/share/doc/HTML/es/kdiff3/index.cache.bz2
/usr/share/doc/HTML/es/kdiff3/index.docbook
/usr/share/doc/HTML/it/kdiff3/index.cache.bz2
/usr/share/doc/HTML/it/kdiff3/index.docbook
/usr/share/doc/HTML/nl/kdiff3/index.cache.bz2
/usr/share/doc/HTML/nl/kdiff3/index.docbook
/usr/share/doc/HTML/sv/kdiff3/index.cache.bz2
/usr/share/doc/HTML/sv/kdiff3/index.docbook
/usr/share/doc/HTML/uk/kdiff3/index.cache.bz2
/usr/share/doc/HTML/uk/kdiff3/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/kfileitemaction/kdiff3fileitemaction.so
/V3/usr/lib64/qt5/plugins/kf5/parts/kdiff3part.so
/usr/lib64/qt5/plugins/kf5/kfileitemaction/kdiff3fileitemaction.so
/usr/lib64/qt5/plugins/kf5/parts/kdiff3part.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdiff3/47c547529aa3a83793060dc46dd05d2eb284de83
/usr/share/package-licenses/kdiff3/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kdiff3/6c284580296aa36e06810ccb61e130fc422eb4d4
/usr/share/package-licenses/kdiff3/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kdiff3/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kdiff3/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kdiff3.1
/usr/share/man/de/man1/kdiff3.1
/usr/share/man/es/man1/kdiff3.1
/usr/share/man/it/man1/kdiff3.1
/usr/share/man/man1/kdiff3.1
/usr/share/man/nl/man1/kdiff3.1
/usr/share/man/sv/man1/kdiff3.1
/usr/share/man/uk/man1/kdiff3.1

%files locales -f kdiff3.lang -f diff_ext.lang -f kdiff3fileitemactionplugin.lang
%defattr(-,root,root,-)

