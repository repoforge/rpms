# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-UI

Summary: Term::ReadLine UI made easy
Name: perl-Term-UI
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-UI/

Source: http://www.cpan.org/modules/by-module/Term/Term-UI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Term::UI provides methods to ask both elaborate questions as well
as simple yes/no questions via a Term::ReadLine interface using a
template. It can also parse options per unix style.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Term/
%{perl_vendorlib}/Term/UI.pm
%dir %{perl_vendorlib}/Term/UI
%{perl_vendorlib}/Term/UI/History.pm

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
