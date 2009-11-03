# $Id$
# Authority: dries
# Upstream: Brandon L. Black <blblack$gmail,com>
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Algorithm-C3

Summary: Module for merging hierarchies using the C3 algorithm
Name: perl-Algorithm-C3
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Algorithm-C3/

Source: http://www.cpan.org/modules/by-module/Algorithm/Algorithm-C3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp) >= 0.01
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More) >= 0.47


%description
C3 is the name of an algorithm which aims to provide a sane method
resolution order under multiple inheritence. It was first introduced
in the langauge Dylan (see links in the L<SEE ALSO> section), and
then later adopted as the preferred MRO (Method Resolution Order)
for the new-style classes in Python 2.3. Most recently it has been
adopted as the 'canonical' MRO for Perl 6 classes, and the default
MRO for Parrot objects as well.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Algorithm::C3.3pm*
%dir %{perl_vendorlib}/Algorithm/
#%{perl_vendorlib}/Algorithm/C3/
%{perl_vendorlib}/Algorithm/C3.pm

%changelog
* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Sat Jul 15 2006 Al Pacifico <adpacifico@users.sourceforge.net> - 0.05-1
- Initial packaging
