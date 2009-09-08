# $Id$
# Authority: dag
# Upstream: David Coppit <david@coppit.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Mbox-MessageParser

Summary: Fast and simple mbox folder reader
Name: perl-Mail-Mbox-MessageParser
Version: 1.5002
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Mbox-MessageParser/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Mbox-MessageParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(FileHandle::Unget)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff)
Requires: perl >= 0:5.004

%description
Mail::Mbox::MessageParser is a fast and simple mbox folder reader.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
echo | %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
echo | %{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/Mbox/
%{perl_vendorlib}/Mail/Mbox/MessageParser/
%{perl_vendorlib}/Mail/Mbox/MessageParser.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 1.5002-1
- Updated to version 1.5002.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.5000-1
- Updated to release 1.5000.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.4005-1
Updated to release 1.4005.

* Tue May 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.4003-1
- Updated to release 1.4003.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4002-1.2
- Rebuild for Fedora Core 5.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.4002-1
- Updated to release 1.4002.

* Sat Aug 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.4001-1
- Updated to release 1.4001.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 1.2130-1
- Initial package. (using DAR)
