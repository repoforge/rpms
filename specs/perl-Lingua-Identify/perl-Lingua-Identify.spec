# $Id$
# Authority: dries
# Upstream: Jos&#233; Alves de Castro <cog$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Identify

Summary: Identify languages
Name: perl-Lingua-Identify
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Identify/

Source: http://search.cpan.org/CPAN/authors/id/C/CO/COG/Lingua-Identify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl

%description
A module which can identify languages.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/langident
%{_bindir}/make-lingua-identify-language
%{perl_vendorlib}/Lingua/Identify.pm
%{perl_vendorlib}/Lingua/Identify/

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
