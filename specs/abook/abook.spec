# $Id$
# Authority: shuff
# Upstream: Jaakko Heinonen <jheinonen$users,sourceforge,net>

Summary: Text-based addressbook
Name: abook
Version: 0.5.6
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://abook.sourceforge.net/

Source: http://prdownloads.sourceforge.net/abook/abook-%{version}.tar.gz
Patch0: abook-0.5.6_editor.patch
Patch1: abook_vcard_import.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: rpm-macros-rpmforge

# don't scan the contrib for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

%filter_setup

%description
Abook is a text-based addressbook program designed to use with the mutt mail
client.

%prep
%setup
%patch0 -p1
# the vCard patch doesn't apply cleanly
# %patch1 -p1

%build
%configure \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ABOUT-NLS ANNOUNCE AUTHORS BUGS ChangeLog COPYING FAQ INSTALL NEWS 
%doc README THANKS TODO doc/* contrib/
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Tue Aug 23 2011 Steve Huff <shuff@vecna.org> - 0.5.6-1
- Initial package.
