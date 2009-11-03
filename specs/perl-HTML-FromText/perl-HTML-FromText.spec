# $Id$
# Authority: dag
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-FromText

Summary: Perl module to convert plain text to HTML
Name: perl-HTML-FromText
Version: 2.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-FromText/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-FromText-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-HTML-FromText is a Perl module to convert plain text to HTML.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man1/text2html.1*
%doc %{_mandir}/man3/HTML::FromText.3pm*
%{_bindir}/text2html
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/FromText.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 2.05-1
- Initial package. (using DAR)
