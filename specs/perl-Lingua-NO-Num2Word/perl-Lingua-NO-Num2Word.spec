# $Id$
# Authority: dries
# Upstream: Kjetil Fikkan <kjetil$fikkan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-NO-Num2Word

Summary: Convert numbers to norwegian textual representation
Name: perl-Lingua-NO-Num2Word
Version: 0.011
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-NO-Num2Word/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KACCV/Lingua-NO-Num2Word-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
OO module for converting positiv whole numbers into its
norwegian textual representation. 

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Lingua/NO/Num2Word.pm

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.011-1
- Initial package.
