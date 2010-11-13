# $Id$
# Authority: dag

Summary: Archiver and compressor
Name: freeze
Version: 2.5.0
Release: 1.2%{?dist}
License: distributable
Group: Applications/Archiving
URL: ftp://ftp.std.com/src/util/

Source: http://www.ibiblio.org/pub/Linux/utils/compress/freeze-%{version}.tar.gz
Patch0: freeze-2.5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Freeze is an old file compressor and decompressor that is not in
common use anymore, but can be useful if the need ever arises to
dearchive files compressed with it.

%prep
%setup
%patch

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
%doc MANIFEST README
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 2.5.0-1
- Update to latest found version 2.5.0.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 2.5-2
- Cosmetic rebuild for Group-tag.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
