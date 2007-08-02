# $Id$

# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>


%define real_name XML-XPath
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Parse and evaluate XPath statements
Name: perl-XML-XPath
Version: 1.13
Release: 2.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-XPath/

Source: http://www.cpan.org/modules/by-module/XML/XML-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added
in the form of functions. Modules such as XSLT and XPointer may
need to do this as they support functionality beyond XPath.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO
%{_bindir}/xpath
%{_mandir}/man3/*
%{perl_vendorlib}/XML/XPath.pm
%{perl_vendorlib}/XML/XPath/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-2.2
- Rebuild for Fedora Core 5.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-2
- Fixed the license tag (Thanks to David Necas !)

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.
