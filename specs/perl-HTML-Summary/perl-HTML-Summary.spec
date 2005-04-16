# $Id$
# Authority: dries
# Upstream: Tony G. Rose <tgr$cre,canon,co,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Summary

Summary: Generating a summary from a web page
Name: perl-HTML-Summary
Version: 0.017
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Summary/

Source: http://search.cpan.org/CPAN/authors/id/T/TG/TGROSE/HTML-Summary-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The HTML::Summary module produces summaries from the textual content of
web pages. It does so using the location heuristic, which determines the value
of a given sentence based on its position and status within the document; for
example, headings, section titles and opening paragraph sentences may be
favoured over other textual content. A LENGTH option can be used to restrict
the length of the summary produced.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/Summary.pm
%{perl_vendorlib}/Lingua/JA
%{perl_vendorlib}/Text/Sentence.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.017-1
- Initial package.
