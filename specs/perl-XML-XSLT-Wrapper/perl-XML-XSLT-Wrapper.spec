# $Id$
# Authority: dag
# Upstream: Colin Muller <colin$durbanet,co,za>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-XSLT-Wrapper

Summary: Perl module that implements a consistent interface to XSLT processors
Name: perl-XML-XSLT-Wrapper
Version: 0.32
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-XSLT-Wrapper/

Source: http://www.cpan.org/modules/by-module/XML/XML-XSLT-Wrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-XSLT-Wrapper is a Perl module that implements a consistent interface
to XSLT processors.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO examples/
%doc %{_mandir}/man3/XML::XSLT::Wrapper.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/XSLT/
%{perl_vendorlib}/XML/XSLT/Wrapper.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Initial package. (using DAR)
