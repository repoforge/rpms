# $Id$
# Authority: dries
# Upstream: Peter Thatcher <peterthatcher$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Latex

Summary: Creates a Latex file from an HTML file
Name: perl-HTML-Latex
Version: 1.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Latex/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETER/HTML-Latex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Converts properly formatted HTML files, filehandles, or strings to
LaTeX.  It offers several options in processing, such a the ignoring
of tags, the configuration of the TeX, and downloading of URLs.  It is
also much easier to extend than any other html2latex converter.

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
%{perl_vendorlib}/HTML/Latex.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
