# $Id$
# Authority: dries
# Upstream: Kaelin Colclasure <kaelin$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Subtext

Summary: Perform text substitutions on an HTML template
Name: perl-HTML-Subtext
Version: 1.03
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Subtext/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Subtext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is designed to do simple textual substitutions into an
HTML template document in an "offline" process. It is *not* a
mechanism for implementing server-side includes -- there are plenty of
other perl modules that do that. There are also other modules which
let you embed arbitrary perl expressions in a template. [These are
quite powerful and useful, but assume a certain sophistication on the
part of the template author.] HTML::Subtext doesn't do that either.

What it does do is allow you to compose an HTML document using your
favorite WYSIWYG HTML editor, include place-holder strings in it like
"Customer's name here", and then turn those place holders into a
substitution field by making the text a link to a special 'subtext:'
URI.

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
%{perl_vendorlib}/HTML/Subtext.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
