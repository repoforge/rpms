# $Id$
# Authority: dag
# Upstream: Yuval Kogman <nothingmuch$woobling,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Cookie-Splitter

Summary: Perl module to split big cookies into smaller ones
Name: perl-CGI-Cookie-Splitter
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Cookie-Splitter/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Cookie-Splitter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-CGI-Cookie-Splitter is a Perl module to split big cookies
into smaller ones.

This package contains the following Perl module:

    CGI::Cookie::Splitter

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
%doc Changes MANIFEST META.yml SIGNATURE
%doc %{_mandir}/man3/CGI::Cookie::Splitter.3pm*
%dir %{perl_vendorlib}/CGI/
%dir %{perl_vendorlib}/CGI/Cookie/
#%{perl_vendorlib}/CGI/Cookie/Splitter/
%{perl_vendorlib}/CGI/Cookie/Splitter.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
