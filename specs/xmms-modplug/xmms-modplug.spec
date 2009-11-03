# $Id$
# Authority: dag

%define xmms_inputdir %(xmms-config --input-plugin-dir)

%define real_name modplugxmms

Summary: MOD music file plugin for XMMS
Name: xmms-modplug
Version: 2.05
Release: 1.2%{?dist}
License: Public Domain
Group: Applications/Multimedia
URL: http://modplug-xmms.sourceforge.net/

Source: http://dl.sf.net/modplug-xmms/modplugxmms-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, xmms-devel, gtk+-devel, libmodplug-devel
BuildRequires: gcc-c++
Requires: xmms

%description
xmms-modplug is a fully featured, complete input plugin for XMMS which
plays mod-like music formats.

%package -n modplugplay
Summary: Command line mod player
Group: Applications/Multimedia

%description -n modplugplay
A command line mod player.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" XMMS_INPUT_PLUGIN_DIR="%{xmms_inputdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{xmms_inputdir}/libmodplugxmms.so
%exclude %{xmms_inputdir}/libmodplugxmms.la

%files -n modplugplay
%defattr(-, root, root, 0755)
%{_bindir}/modplugplay

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.05-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 06 2005 Dag Wieers <dag@wieers.com> - 2.05-1
- Initial package. (using DAR)
