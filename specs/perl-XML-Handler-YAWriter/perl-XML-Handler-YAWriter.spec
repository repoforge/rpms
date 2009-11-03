# $Id$
# Authority: dries
# Upstream: Michael Koehne <kraehe$copyleft,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Handler-YAWriter

Summary: Yet another Perl SAX XML Writer
Name: perl-XML-Handler-YAWriter
Version: 0.23
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Handler-YAWriter/

Source: http://www.cpan.org/modules/by-module/XML/XML-Handler-YAWriter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man1/xmlpretty.1*
%doc %{_mandir}/man3/XML::Handler::YAWriter.3pm*
%{_bindir}/xmlpretty
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Handler/
%{perl_vendorlib}/XML/Handler/YAWriter.pm

%changelog
* Sat Apr 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Initial package.
