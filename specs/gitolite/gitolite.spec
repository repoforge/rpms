%global perl_vendorlib %(eval $(perl -V:vendorlib); echo $vendorlib)
# RHEL uses %%{_prefix}/com for %{_sharedstatedir} instead of /var/lib
%if 0%{?rhel}
%global gitolite_homedir /var/lib/%{name}
%else
%global gitolite_homedir %{_sharedstatedir}/%{name}
%endif

Name:           gitolite
Version:        2.0.3
Release:        3%{?dist}
Summary:        Highly flexible server for git directory version tracker

Group:          Applications/System
License:        GPLv2
URL:            http://github.com/sitaramc/gitolite
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# $ git clone git://github.com/sitaramc/gitolite.git gitolite
# $ cd gitolite
# $ git archive ed2bf5 |gzip >gitolite-ed2bf5.tar.gz
#Source0:        gitolite-ed2bf5.tar.gz
Source0:        gitolite-2.0.3.tar.gz
#Source1:        gitolite-README-fedora
# Far from being upstreamable
Patch0:         gitolite-2.0-rpm.patch
#Patch1:         gitolite-1.4.2-conf.patch
#Patch2:         adcfix.post-v2.patch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  perl(Text::Markdown)
# We provide the module, but don't create a package/name space
Provides:       perl(%{name}) = %{version}-%{release}
Requires:       git
Requires:       openssh-clients
Requires:       perl(:MODULE_COMPAT_%(eval $(%{__perl} -V:version); echo $version))
Requires(pre):  shadow-utils

%description
Gitolite allows a server to host many git repositories and provide access
to many developers, without having to give them real userids on the server.
The essential magic in doing this is ssh's pubkey access and the authorized
keys file, and the inspiration was an older program called gitosis.

Gitolite can restrict who can read from (clone/fetch) or write to (push) a
repository. It can also restrict who can push to what branch or tag, which
is very important in a corporate environment. Gitolite can be installed
without requiring root permissions, and with no additional software than git
itself and perl. It also has several other neat features described below and
elsewhere in the doc/ directory.


%prep
%setup -qn sitaramc-gitolite-4c1e4b2
# Don't create backups; would mess with %%install
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#cp %{SOURCE1} .


%build
#Drop gl-easy-install per upstream.
rm -f src/gl-easy-install
# Format documentation
for F in doc/*.mkd
do
        perl -MText::Markdown >$(echo $F |sed s/.mkd/.html/) <$F \
                -e 'print Text::Markdown::markdown (join "", <>)'
done


%install
rm -rf $RPM_BUILD_ROOT

# Directory structure
install -d $RPM_BUILD_ROOT%{gitolite_homedir}
install -d $RPM_BUILD_ROOT%{gitolite_homedir}/.ssh
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

# Code
install -p src/gl-* $RPM_BUILD_ROOT%{_bindir}
install -p -m644 src/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}
cp -a conf hooks $RPM_BUILD_ROOT%{_datadir}/%{name}

# empty authorized_keys file
touch $RPM_BUILD_ROOT%{gitolite_homedir}/.ssh/authorized_keys

 
%clean
rm -rf $RPM_BUILD_ROOT


%pre
# Add "gitolite" user per https://fedoraproject.org/wiki/Packaging:UsersAndGroups
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
useradd -r -g %{name} -d %{gitolite_homedir} -s /bin/sh \
        -c "git repository hosting" %{name}
exit 0


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}
# make homedir non world readable
%attr(750,%{name},%{name}) %{gitolite_homedir}
%attr(750,%{name},%{name}) %{gitolite_homedir}/.ssh
%config(noreplace) %attr(640,%{name},%{name}) %{gitolite_homedir}/.ssh/authorized_keys
%doc doc/COPYING doc/*.html 
#gitolite-README-fedora


%changelog
* Thu Oct 13 2011 David Hrbáč <david@hrbac.cz> - 2.0.3-3
- added missing patch

* Thu Sep 22 2011 David Hrbáč <david@hrbac.cz> - 2.0.3-2
- initial rebuild

* Mon Aug 08 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.3-2
- Updated rpm patch to fix hooks, BZ 713020.

* Mon Aug 08 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.3-1
- New upstream.

* Wed Aug 03 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.2-3
- Updated rpm patch to fix hooks, BZ 713020.

* Tue Jun 21 2011 Marcela MaÅ¡lÃ¡ÅˆovÃ¡ <mmaslano@redhat.com> - 2.0.2-2
- Perl mass rebuild

* Wed Jun 01 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.2-1
- New upstream.

* Mon May 02 2011 Jon Ciesla <limb@jcomserv.net> - 2.0.1-1
- New upstream.

* Fri Mar 11 2011 Jon Ciesla <limb@jcomserv.net> - 2.0-1
- New upstream.

* Thu Feb 17 2011 Jon Ciesla <limb@jcomserv.net> - 1.5.9.1-1
- New upstream.
- ADC patch upstreamed.

* Tue Feb 15 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.5.9-2
- Fix ADC security issue

* Mon Feb 14 2011 Jon Ciesla <limb@jcomserv.net> - 1.5.9-1
- New upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.8-1
- New upstream.

* Sat Nov 06 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.7-1
- New upstream.

* Mon Oct 18 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.6-1
- New upstream.

* Fri Aug 27 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.5-1
- New upstream.

* Fri Jul 30 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.4-1
- New upstream.

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.3-1
- New upstream.

* Mon Jun 14 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.2-1
- New upstream.

* Wed Jun 02 2010 Jon Ciesla <limb@jcomserv.net> - 1.5.1-1
- New upstream, prevents having to run gl-setup as gitolite user.

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.5-2
- Mass rebuild with perl-5.12.0

* Thu May 20 2010 Jon Ciesla <limb@jcomserv.net> - 1.5-1
- Update to 1.5.

* Fri Apr 23 2010 Jon Ciesla <limb@jcomserv.net> - 1.4.2-1
- Update to 1.4.2.
- Replaced README and removed gl-easy-install per upstream.

* Tue Mar 23 2010 Jon Ciesla <limb@jcomserv.net> - 1.3-1
- Update to 1.3, BZ 576233.
- Updated rpm and conf patches accordingly.

* Tue Feb 09 2010 Till Maas <opensource@till.name> - 0.95-4.20091216git
- RHEL defines %%{_sharedstatedir} to be %%{_prefix}/com, so use a %%global
  redirection to set the homedir to a proper value (/var/lib).
  Red Hat Bug #185862
- add missing exit 0 to %%pre
- Update wiki UserAndGroups Url to the redirection target
- create empty authorized_keys file for gitolite user
- make homedir not world readable

* Thu Jan 21 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.95-3.20091216git
- Add documentation
- Rename upstream tarball

* Wed Dec 16 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.95-2.20091216git
- Rename patch
- Fix path to post-update hook
- Make example configuration compilable

* Wed Dec 16 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.95-1.20091216git
- Initial packaging

