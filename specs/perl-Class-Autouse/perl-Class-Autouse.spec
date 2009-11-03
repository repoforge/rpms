# $Id$
# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Autouse

Summary: Run-time class loading on first method call
Name: perl-Class-Autouse
Version: 1.29
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Autouse/

Source: http://www.cpan.org/modules/by-module/Class/Class-Autouse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005 
BuildRequires: perl(Carp) >= 1.01
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(List::Util) >= 1.18
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005 

#Test-Simple and Scalar-List-Utils is already included in the perl package on fedora core

%description
Class::Autouse allows you to specify a class the will only load when a
method of that class is called. For large classes that might not be used
during the running of a program, such as Date::Manip, this can save you
large amounts of memory, and decrease the script load time.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man3/Class::Autouse.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Autouse/
%{perl_vendorlib}/Class/Autouse.pm
#%{perl_vendorlib}/Class/prefork.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.29-1
- Updated to release 1.29.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Thu Jun 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.26-1
- Updated to release 1.26.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Updated to release 1.24.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
