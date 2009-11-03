# $Id$
# Authority: dries
# Upstream: Gerald Richter <richter$ecos,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Push

Summary: Push Repository to Remote Subversion Repository
Name: perl-SVN-Push
Version: 0.02
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Push/

Source: http://www.cpan.org/modules/by-module/SVN/SVN-Push-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: subversion-perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
SVN::Push is a module which let you push the content of a repoitory
or a parts of a repository to another subversion repository, using the
Ra layer. This means you can access the repositories by URL, so
it works also with remote repositories. It's also possible to specify
the revisions to push, so you need not to copy all revision and can
instead just push a cumulated revision, where necessary.

svnpush is a command line frontend for SVN::Push.

svndumpload is a command line tool which is able to replicate
a full repository to another by doing incremental dumps and loads.
It checks the revsion of the destination repsitory and
dumps only changes. One or both repositories could
be on a remote machine, in which case ssh access is necessary.
The main adavatage of svndumpload over svnpush is that it preserves
copy history.

svnsetuuid is a command line tool to set the uuid of a repostory.
This is necessary in case you want later on your working copy
with svn switch --relocate, in which case both repositories need to
have the same uuid.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/*
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Push.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
