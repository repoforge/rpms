# $Id$
# Authority: dries
# Upstream: Burak G&#252;rsoy <burak$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Template-Simple

Summary: Simple text template engine
Name: perl-Text-Template-Simple
Version: 0.47
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Template-Simple/

Source: http://search.cpan.org//CPAN/authors/id/B/BU/BURAK/Text-Template-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Simple text template engine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Template/Simple.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Updated to release 0.47.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.46-1
- Updated to release 0.46.

* Wed Sep 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Updated to release 0.44.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
