# $Id$
# Authority: dries
# Upstream: Ryuzo Yamamoto <ryuzo,yamamoto$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-DBIC-Schema-Profiler

Summary: Profile DBIC::Schema queries in Catalyst
Name: perl-Catalyst-Plugin-DBIC-Schema-Profiler
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-DBIC-Schema-Profiler/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-DBIC-Schema-Profiler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Profile DBIC::Schema queries in Catalyst.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Catalyst::Plugin::DBIC::Schema::Profiler.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/DBIC/
%dir %{perl_vendorlib}/Catalyst/Plugin/DBIC/Schema/
%{perl_vendorlib}/Catalyst/Plugin/DBIC/Schema/Profiler/
%{perl_vendorlib}/Catalyst/Plugin/DBIC/Schema/Profiler.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
