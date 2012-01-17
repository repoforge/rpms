# $Id$
# Authority: dag

Summary: freeze/melt/fcat compression utilities
Name: freeze
Version: 2.5.0
Release: 3%{?dist}
License: GPL+
Group: Applications/Archiving
URL: ftp://ftp.std.com/src/util/

Source: http://www.ibiblio.org/pub/Linux/utils/compress/freeze-%{version}.tar.gz
Source1: Freeze_license_email.txt
Patch0: freeze-2.5.patch
Patch1: freeze-2.5.0-printf.patch
Patch2: freeze-2.5.0-deffile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Freeze is an old file compressor and decompressor that is not in
common use anymore, but can be useful if the need ever arises to
dearchive files compressed with it.

%prep
%setup
cp -a %{SOURCE1} .
%patch0 -p0
%patch1 -p1 -b .printf
%patch2 -p1 -b .deffile

%build
%{__chmod} u+x configure
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall \
	MANDEST="%{buildroot}%{_mandir}/man1/"

### Fix symlinks properly
for bin in fcat melt unfreeze; do
	%{__ln_s} -f freeze %{buildroot}%{_bindir}/$bin
	%{__rm} -f %{buildroot}%{_mandir}/man1/$bin.1
	%{__ln_s} -f freeze.1.gz %{buildroot}%{_mandir}/man1/$bin.1.gz
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README Freeze_license_email.txt
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Tue Jan 17 2012 David Hrbáč <david@hrbac.cz> - 2.5.0-3
- Fix bad printf string (#149613).
- Fix default cnf file location in readme and man page.

* Tue Jan 17 2012 David Hrbáč <david@hrbac.cz> - 2.5.0-2
- corrected for EL6 build

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1
- Update to latest found version 2.5.0.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 2.5-2
- Cosmetic rebuild for Group-tag.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
