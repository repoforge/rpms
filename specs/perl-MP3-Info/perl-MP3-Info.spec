# $Id$
# Authority: dries
# Upstream: Dan Sully <daniel$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MP3-Info

Summary: Edit MP3 tags
Name: perl-MP3-Info
Version: 1.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MP3-Info/

Source: http://www.cpan.org/modules/by-module/MP3/MP3-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can read and edit information within MP3 files.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes Info.pm MANIFEST README TODO eg/
%doc %{_mandir}/man3/MP3::Info.3pm*
%dir %{perl_vendorlib}/MP3/
#%{perl_vendorlib}/MP3/Info/
%{perl_vendorlib}/MP3/Info.pm
#%{perl_vendorlib}/MPEG/MP3Info.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.24-1
- Updated to version 1.24.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
