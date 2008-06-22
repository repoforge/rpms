# Authority: dries
# Upstream: Steve Purkis <spurkis$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name accessors

Summary: Create accessor methods in caller's package
Name: perl-accessors
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/accessors/

Source: http://www.cpan.org/authors/id/S/SP/SPURKIS/accessors-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Module::Build) >= 0.2
BuildRequires: perl(Test::More) >= 0.01
Requires: perl >= 0:5.6.0

%description
The accessors pragma lets you create simple accessors at compile-time.

This saves you from writing them by hand, which tends to result in
*cut-n-paste* errors and a mess of duplicated code. It can also help you
reduce the ammount of unwanted *direct-variable access* that may creep
into your codebase when you're feeling lazy. accessors was designed with
laziness in mind.

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
%doc Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/accessors.3pm*
%doc %{_mandir}/man3/accessors::*.3pm*
%{perl_vendorlib}/accessors/
%{perl_vendorlib}/accessors.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
