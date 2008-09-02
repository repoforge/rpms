# $Id$
# Authority: dag
# Upstream: Andy Grundman, <andy@hybridized.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Static-Simple

Summary: Make serving static pages painless
Name: perl-Catalyst-Plugin-Static-Simple
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Static-Simple/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Static-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime), perl(File::Slurp), perl(MIME::Types)

%description
Make serving static pages painless.

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
%doc %{_mandir}/man3/Catalyst::Plugin::Static::Simple.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Static/
#%{perl_vendorlib}/Catalyst/Plugin/Static/Simple/
%{perl_vendorlib}/Catalyst/Plugin/Static/Simple.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
