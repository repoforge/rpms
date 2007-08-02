# $Id$
# Authority: dries
# Upstream: Steve Purkis <spurkis%20%5bat%5d%20quiup_dot_com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name accessors

Summary: Create accessor methods
Name: perl-accessors
Version: 0.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/accessors/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPURKIS/accessors-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

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
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/accessors.pm
%{perl_vendorlib}/accessors/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
