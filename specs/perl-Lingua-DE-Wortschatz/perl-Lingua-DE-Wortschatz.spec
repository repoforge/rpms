# $Id$
# Authority: dries
# Upstream: Daniel Schr&#246;er <schroeer$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-DE-Wortschatz

Summary: Wortschatz.uni-leipzig.de webservice client
Name: perl-Lingua-DE-Wortschatz
Version: 1.23
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-DE-Wortschatz/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCHROEER/Wortschatz/Lingua-DE-Wortschatz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
Wortschatz.uni-leipzig.de webservice client.

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
%doc README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/wsws.pl
%{perl_vendorlib}/Lingua/DE/Wortschatz.pm

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Initial package.
