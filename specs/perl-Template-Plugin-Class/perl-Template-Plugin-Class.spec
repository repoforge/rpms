# $Id$
# Authority: dag
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-Class

Summary: Allow calling of class methods on arbitrary classes
Name: perl-Template-Plugin-Class
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-Class/

Source: http://www.cpan.org/modules/by-module/Template/Template-Plugin-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
Allow calling of class methods on arbitrary classes.

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
%doc %{_mandir}/man3/Template::Plugin::Class.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Plugin/
%{perl_vendorlib}/Template/Plugin/Class.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.14-1
- Updated to version 0.14.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
