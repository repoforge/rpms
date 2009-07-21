# $Id$
# Authority: dag
# Upstream: Paul Evans E<lt>leonerd$leonerd,org,ukE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Refcount

Summary: assert reference counts on objects
Name: perl-Test-Refcount
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Refcount/

Source: http://www.cpan.org/modules/by-module/Test/Test-Refcount-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)

%description
assert reference counts on objects.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Test::Refcount.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Refcount/
%{perl_vendorlib}/Test/Refcount.pm

%changelog
* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
