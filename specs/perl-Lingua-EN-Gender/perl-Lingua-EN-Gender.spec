# $Id$
# Authority: dries
# Upstream: Eugene Eric Kim <eekim$blueoxen,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-Gender

Summary: Guesses author's gender by analyzing text
Name: perl-Lingua-EN-Gender
Version: 1.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-Gender/

Source: http://search.cpan.org/CPAN/authors/id/E/EE/EEKIM/Lingua-EN-Gender-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lingua::EN::Gender implements the Koppel-Argamon algorithm for
guessing an author's gender.  The algorithm was invented by Moshe
Koppel (Bar-Ilan University, Israel) and Shlomo Argamon (Illinois
Institute of Technology).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Lingua/EN/gender.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
