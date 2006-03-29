# $Id$
# Authority: dries
# Upstream: Michael Koehne <kraehe$copyleft,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Handler-YAWriter

Summary: Yet another Perl SAX XML Writer
Name: perl-XML-Handler-YAWriter
Version: 0.23
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Handler-YAWriter/

Source: http://search.cpan.org/CPAN/authors/id/K/KR/KRAEHE/XML-Handler-YAWriter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
YAWriter implements Yet Another XML::Handler::Writer. The
reasons for this one are that I needed a flexible escaping
technique, and want some kind of pretty printing.

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
%doc %{_mandir}/man?/*
%{_bindir}/xmlpretty
%{perl_vendorlib}/XML/Handler/YAWriter.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
