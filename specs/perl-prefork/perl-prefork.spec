# $Id$
# Authority: dag
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name prefork

Summary: Optimized module loading for forking or non-forking processes
Name: perl-prefork
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/prefork/

Source: http://www.cpan.org/authors/id/A/AD/ADAMK/prefork-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Optimized module loading for forking or non-forking processes.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/prefork.3pm*
%{perl_vendorlib}/prefork.pm

%changelog
* Mon Jun 22 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Updated to version 1.03.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
