# $Id$
# Authority: dag
# Upstream: Sebastian Riedel <sri$oook,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Widget

Summary: HTML Widget And Validation Framework
Name: perl-HTML-Widget
Version: 1.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Widget/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Widget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.1
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Accessor::Chained::Fast)
BuildRequires: perl(Class::Data::Accessor)
BuildRequires: perl(Date::Calc)
BuildRequires: perl(Email::Valid)
BuildRequires: perl(HTML::Element) >= 3.22
BuildRequires: perl(HTML::Scrubber)
BuildRequires: perl(HTML::Tree)
BuildRequires: perl(Module::Pluggable::Fast)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::NoWarnings)
Requires: perl >= 2:5.8.1

%description
HTML Widget And Validation Framework.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/HTML::Widget.3pm*
%doc %{_mandir}/man3/HTML::Widget::*.3pm*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/Widget/
%{perl_vendorlib}/HTML/Widget.pm

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.11-1
- Initial package. (using DAR)
