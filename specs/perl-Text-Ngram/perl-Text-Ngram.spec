# $Id$
# Authority: dries
# Upstream: Jos&#233; Alves de Castro <cog$cpan,org>

%define debug_package %{nil}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Ngram

Summary: Ngram analysis of text
Name: perl-Text-Ngram
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Ngram/

Source: http://search.cpan.org/CPAN/authors/id/C/CO/COG/Text-Ngram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Ngram analysis of text.

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
#%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Text/Ngram.pm
%{perl_vendorarch}/auto/Text/Ngram/

%changelog
* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
