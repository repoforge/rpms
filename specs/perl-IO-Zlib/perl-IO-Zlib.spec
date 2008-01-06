# $Id$
# Authority: dries
# Upstream: Tom Hughes <tom$compton,nu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Zlib

Summary: IO:: interface to Compress::Zlib
Name: perl-IO-Zlib
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Zlib/

Source: http://www.cpan.org/modules/by-module/IO/IO-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This modules provides an IO:: style interface to the Compress::Zlib
package. The main advantage is that you can use an IO::Zlib object
in much the same way as an IO::File object so you can have common
code that doesn't know which sort of file it is using.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/IO::Zlib.3pm*
%dir %{perl_vendorlib}/IO/
#%{perl_vendorlib}/IO/Zlib/
%{perl_vendorlib}/IO/Zlib.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
