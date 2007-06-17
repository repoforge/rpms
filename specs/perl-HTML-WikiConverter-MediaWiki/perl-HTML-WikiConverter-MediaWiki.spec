# $Id$
# Authority: dries
# Upstream: David Iberri <diberri$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-WikiConverter-MediaWiki

Summary: Converts HTML to MediaWiki markup
Name: perl-HTML-WikiConverter-MediaWiki
Version: 0.55
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-WikiConverter-MediaWiki/

Source: http://search.cpan.org//CPAN/authors/id/D/DI/DIBERRI/HTML-WikiConverter-MediaWiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
HTML::WikiConverter::MediaWiki adds the MediaWiki dialect to
HTML::WikiConverter allowing the conversion of HTML to MediaWiki
markup.

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
%dir %{perl_vendorlib}/HTML/WikiConverter/
%{perl_vendorlib}/HTML/WikiConverter/MediaWiki.pm

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Initial package.
