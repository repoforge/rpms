# $Id$
# Authority: dries
# Upstream: Oliver Gorwits <oliver,gorwits$oucs,ox,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Appliance-Phrasebook

Summary: Network appliance command-line phrasebook
Name: perl-Net-Appliance-Phrasebook
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Appliance-Phrasebook/

Source: http://www.cpan.org/modules/by-module/Net/Net-Appliance-Phrasebook-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Network appliance command-line phrasebook.

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Net::Appliance::Phrasebook.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/Appliance/
#%{perl_vendorlib}/Net/Appliance/Phrasebook/
%{perl_vendorlib}/Net/Appliance/Phrasebook.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
