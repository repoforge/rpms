# $Id$
# Authority: dries
# Upstream: Paul Marquess <pmqs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Compress-Base

Summary: Base Class for IO::Compress modules
Name: perl-IO-Compress-Base
Version: 2.003
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Compress-Base/

Source: http://search.cpan.org//CPAN/authors/id/P/PM/PMQS/IO-Compress-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Base Class for IO::Compress modules.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/IO::Compress::Base*
%doc %{_mandir}/man3/IO::Uncompress::*
%doc %{_mandir}/man3/File::GlobMapper*
%{perl_vendorlib}/IO/Compress/Base.pm
%{perl_vendorlib}/IO/Compress/Base/
%{perl_vendorlib}/IO/Uncompress/
%{perl_vendorlib}/File/GlobMapper.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.003-1
- Initial package.

