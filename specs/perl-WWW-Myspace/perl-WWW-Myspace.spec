# $Id$
# Authority: dries
# Upstream: Grant Grueninger <grantg$spamarrest,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Myspace

Summary: Access MySpace.com from perl
Name: perl-WWW-Myspace
Version: 0.58
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Myspace/

Source: http://search.cpan.org//CPAN/authors/id/G/GR/GRANTG/WWW-Myspace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
WWW::Myspace.pm provides methods to access myspace.com accounts and functions
automatically. It provides a simple interface for scripts to log in,
access lists of friends, scan user's profiles, retreive profile
data, and post comments.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/add_friends*
%doc %{_mandir}/man1/approve_friends*
%doc %{_mandir}/man1/comment_myspace*
%doc %{_mandir}/man1/message_group*
%{_bindir}/add_friends
%{_bindir}/approve_friends
%{_bindir}/comment_myspace
%{_bindir}/message_group
%{perl_vendorlib}/WWW/Myspace.pm
%{perl_vendorlib}/WWW/Myspace/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Initial package.
