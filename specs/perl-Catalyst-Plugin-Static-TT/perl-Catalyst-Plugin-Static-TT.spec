# $Id$
# Authority: dag
# Upstream: Hans Dieter Pearcey <hdp$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Static-TT

Summary: Generate 'static' content with TT
Name: perl-Catalyst-Plugin-Static-TT
Version: 0.002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Static-TT/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Static-TT-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)

%description
Generate 'static' content with TT.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Catalyst::Plugin::Static::TT.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Static/
#%{perl_vendorlib}/Catalyst/Plugin/Static/TT/
%{perl_vendorlib}/Catalyst/Plugin/Static/TT.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.002-1
- Initial package. (using DAR)
