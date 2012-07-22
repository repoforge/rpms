# $Id$
# Authority: shuff
# Upstream: Joe Laffey <software$laffeycomputer.com>

Summary: Anti-idle timeout preventer
Name: spinner
Version: 1.2.4
Release: 1%{?dist}
License: GPL
Group: Applications/Utilities
URL: http://www.laffeycomputer.com/spinner.html

Source: http://downloads.laffeycomputer.com/current_builds/spinner/spinner-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
Spinner is an anti-idle program that displays a little "spinning" ASCII
character in the top left corner of your terminal. To make this effect it
cycles through punctuation marks like this " - \ | / - \ | / ... " (try it to
see). By default the character is drawn in inverse video (or your terminal's
equivalent). But you can turn this off with the -i switch. In spinner mode
Spinner supports any terminal capable of handling VT100 style escape codes. In
null mode (-n switch) Spinner supports any terminal. In null mode there is no
visible output, and Spinner will not interfere with your terminal or
scrollback. If you find the little spinner in the top left corner to be
distracting use null mode. (-n switch).

Spinner is useful for keeping telnet and ssh links from dropping due to
inactivity. Many firewalls, and some ISPs drop connections when they are
perceived as idle. By having spinner running the server is constantly sending a
tiny amount of data over the link, preserving the connection. As of version 1.2
Spinner can also be activated with the -n switch so that, instead of displaying
a spinner, it simply sends out a periodic null character to the terminal. This
achieves the same anti-idle benefit without disturbing your screen. But it
lacks the coolness factor of a little spinner in the corner of the terminal...

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*

%changelog
* Tue May  8 2012 Steve Huff <shuff@vecna.org> - 1.2.4-1
- Initial package.
