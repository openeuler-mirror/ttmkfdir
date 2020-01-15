Summary: Utility to create fonts.scale files for truetype fonts
Name:    ttmkfdir
Version: 3.0.9
Release: 56
License: LGPLv2+
Source0: %{name}-%{version}.tar.bz2
Source1: ttmkfdir.1
Patch:   ttmkfdir-3.0.9-cpp.patch
Patch1:  ttmkfdir-3.0.9-zlib.patch
Patch2:  ttmkfdir-3.0.9-fix-freetype217.patch
Patch3:  ttmkfdir-3.0.9-namespace.patch
Patch4:  ttmkfdir-3.0.9-fix-crash.patch
Patch5:  ttmkfdir-3.0.9-warnings.patch
Patch6:  ttmkfdir-3.0.9-segfaults.patch
Patch7:  ttmkfdir-3.0.9-encoding-dir.patch
Patch8:  ttmkfdir-3.0.9-font-scale.patch
Patch9:  ttmkfdir-3.0.9-bug434301.patch
Patch10: ttmkfdir-3.0.9-freetype-header-fix2.patch

BuildRequires: freetype-devel >= 2.0 flex libtool
BuildRequires: bzip2-devel zlib-devel gcc-c++

%description
ttmkfdir is a utility used to create fonts.scale files in
TrueType font directories in order to prepare them for use
by the font server.

%package_help

%prep
%autosetup -p1

%build
%make_build OPTFLAGS="$RPM_OPT_FLAGS"

%install
%make_install
install -d $RPM_BUILD_ROOT/%{_mandir}/man1/
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{_mandir}/man1/

%files
%{_bindir}/ttmkfdir

%files help
%doc README
%{_mandir}/man1/

%changelog
* Tue Dec 3 2019 mengxian <mengxian@huawei.com> - 3.0.9-56
- Package init
