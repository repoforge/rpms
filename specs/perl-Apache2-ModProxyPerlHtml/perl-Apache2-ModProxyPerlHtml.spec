# $Id:$
# Authority: dries
# Upstream: Darold Gilles <CENSORED>


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache2-ModProxyPerlHtml

Summary: Perl module to rewrite HTML links for a reverse proxy
Name: perl-Apache2-ModProxyPerlHtml
Version: 2.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache2-ModProxyPerlHtml/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAROLD/Apache2/ModProxyPerlHtml/Apache2-ModProxyPerlHtml-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: mod_perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Uncompress::AnyInflate)
BuildRequires: perl(IO::Compress::Deflate)
BuildRequires: perl(IO::Compress::Gzip)
BuildRequires: perl(ModPerl::MM)
Requires: mod_perl
Requires: perl(IO::Uncompress::AnyInflate)
Requires: perl(IO::Compress::Deflate)
Requires: perl(IO::Compress::Gzip)
Requires: perl(ModPerl::MM)

%filter_from_requires /^perl*/d
%filter_setup

%description
Apache2::ModProxyPerlHtml is a mod_perl2 replacement of the Apache2
module mod_proxy_html.c use to rewrite HTML links for a reverse proxy.

Apache2::ModProxyPerlHtml is very simple and has far better
parsing/replacement of URL than the original C code. It also support
meta tag, CSS, and javascript URL rewriting and can be use with
compressed HTTP. You can now replace any code by other, like changing
images name or anything else.

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
%doc Change META.yml README
%doc %{_mandir}/man3/Apache2::ModProxyPerlHtml.3pm*
%dir %{perl_vendorlib}/Apache2/
%{perl_vendorlib}/Apache2/ModProxyPerlHtml.pm

%changelog
* Fri Jan 08 2010 Christoph Maser <cmr@financial.com> - 2.6-1
- Upgrade to release 2.6.

* Wed Dec 31 2008 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Initial package.
