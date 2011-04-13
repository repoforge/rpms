# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

### EL6 ships with perl-HTML-Format-2.04-11.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Format

Summary: Format HTML as plaintext, PostScript or RTF
Name: perl-HTML-Format
Version: 2.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Format/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NIGELM/HTML-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a collection of modules that formats HTML as plaintext,
PostScript or RTF.

This package contains the following Perl module:

    HTML::FormatPS

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/HTML::FormatRTF.3pm*
%doc %{_mandir}/man3/HTML::FormatPS.3pm*
%doc %{_mandir}/man3/HTML::FormatText.3pm*
%doc %{_mandir}/man3/HTML::Formatter.3pm*
%dir %{perl_vendorlib}/HTML/
#%{perl_vendorlib}/HTML/Format/
%{perl_vendorlib}/HTML/FormatRTF.pm
%{perl_vendorlib}/HTML/FormatPS.pm
%{perl_vendorlib}/HTML/FormatText.pm
%{perl_vendorlib}/HTML/Formatter.pm

%changelog
* Tue Apr 05 2011 Denis Fateyev <denis@fateyev.com> - 2.05-1
- Updated to version 2.05.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Initial package.
