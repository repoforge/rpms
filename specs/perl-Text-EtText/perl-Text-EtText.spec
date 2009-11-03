# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-EtText

Summary: Perl module that implements editable-text format for HTML output
Name: perl-Text-EtText
Version: 2.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-EtText/

Source: http://www.cpan.org/modules/by-module/Text/Text-EtText-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Text-EtText is a Perl module that implements editable-text format
for HTML output.

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

### Clean up docs
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP README TODO doc/
%doc %{_mandir}/man1/ethtml2text.1*
%doc %{_mandir}/man1/ettext2html.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/ethtml2text
%{_bindir}/ettext2html
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/EtText/
%{perl_vendorlib}/Text/EtText.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 2.2-1
- Initial package. (using DAR)
