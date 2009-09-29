# $Id$
# Authority: cmr
# Upstream: Hans Dieter Pearcey <hdp@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Object-Array

Summary: array references with accessors
Name: perl-Object-Array
Version: 0.060
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Array/

Source: http://www.cpan.org/modules/by-module/Object/Object-Array-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
Requires: perl >= 1:5.6.1

%description
array references with accessors.

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
%doc %{_mandir}/man3/Object::Array.3pm*
%doc %{_mandir}/man3/Object::Array::Plugin::Builtins.3pm*
%doc %{_mandir}/man3/Object::Array::Plugin::ListMoreUtils.3pm*
%dir %{perl_vendorlib}/Object/
%dir %{perl_vendorlib}/Object/Array/Plugin/Builtins.pm
%dir %{perl_vendorlib}/Object/Array/Plugin/ListMoreUtils.pm
%{perl_vendorlib}/Object/Array.pm


%changelog
* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.060-1
- Initial package. (using DAR)
