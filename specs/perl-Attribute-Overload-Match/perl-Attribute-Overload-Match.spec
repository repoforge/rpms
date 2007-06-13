# $Id$
# Authority: dries
# Upstream: Dmitry Karasik <dmitry$karasik,eu,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Attribute-Overload-Match

Summary: Argument-dependent handlers for overloaded operators
Name: perl-Attribute-Overload-Match
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Attribute-Overload-Match/

Source: http://search.cpan.org//CPAN/authors/id/K/KA/KARASIK/Attribute-Overload-Match-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Argument-dependent handlers for overloaded operators.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Attribute::Overload::Match*
%{perl_vendorlib}/Attribute/Overload/Match.pm
%dir %{perl_vendorlib}/Attribute/Overload/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
