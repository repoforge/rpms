# $Id$
# Authority: dag
# Upstream: The Catalyst Core Team - see http://catalyst.perl.org/

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Devel

Summary: Catalyst Development Tools
Name: perl-Catalyst-Devel
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Devel/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Devel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst) >= 5.7000
BuildRequires: perl(Catalyst::Action::RenderView) >= 0.04
BuildRequires: perl(Catalyst::Plugin::ConfigLoader)
BuildRequires: perl(Catalyst::Plugin::Static::Simple) >= 0.16
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(Module::Install) >= 0.64
BuildRequires: perl(parent)
BuildRequires: perl(Path::Class) >= 0.09
BuildRequires: perl(Template) >= 2.14
BuildRequires: perl(YAML) >= 0.55

%description
Catalyst Development Tools.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Catalyst::Devel.3pm*
%doc %{_mandir}/man3/Catalyst::Helper.3pm*
%doc %{_mandir}/man3/Module::Install::Catalyst.3pm*
%dir %{perl_vendorlib}/Catalyst/
#%{perl_vendorlib}/Catalyst/Devel/
%{perl_vendorlib}/Catalyst/Devel.pm
%{perl_vendorlib}/Catalyst/Helper.pm
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install/Catalyst.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
