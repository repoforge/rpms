# $Id$
# Authority: dries
# Upstream: Georg Bauer <gb$hugo,westfalen,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Request-Form

Summary: Construct HTTP::Request objects for form processing
Name: perl-HTTP-Request-Form
Version: 0.952
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Request-Form/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Request-Form-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is an extension of the HTTP::Request suite. It allows easy
processing of forms in a user agent by filling out fields,
querying fields, selections and buttons and pressing buttons. It
uses HTML::TreeBuilder generated parse trees of documents
(especially the forms parts extracted with extract_links) and
generates it's own internal representation of forms from which
it then generates the request objects to process the form
application.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTTP/Request/Form.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.952-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.952-1
- Initial package.
