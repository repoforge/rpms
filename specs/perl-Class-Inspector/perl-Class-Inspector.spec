# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Inspector

Summary: Get information about a class and its structure
Name: perl-Class-Inspector
Version: 1.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Inspector/

Source: http://www.cpan.org/modules/by-module/Class/Class-Inspector-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
arn't always very friendly, and usually involve a relatively high level
of Perl wizardry, or strange and unusual looking code. Class::Inspector
attempts to provide an easier, more friendly interface to this
information.

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
%doc %{_mandir}/man3/Class::Inspector.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/Inspector/
%{perl_vendorlib}/Class/Inspector.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Sun Jan 16 2005 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.

