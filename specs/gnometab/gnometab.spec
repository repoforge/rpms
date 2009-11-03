# $Id$
# Authority: dag
# Upstream: <jmullins$solutionm,com>
# Upstream: <wguelker$solutionm,com>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: WYSIWIG guitar tablature editor
Name: gnometab
Version: 0.7.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.solutionm.com/gnometab/gnometab.html

Source: http://www.solutionm.com/gnometab/gnometab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.0.3, libgnomeui-devel >= 2.0.0
BuildRequires: libgnomecanvas-devel >= 2.0.0, libgnomeprintui-devel >= 1.0
BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel

%description
Gnometab aims to be a WYSIWYG tablature editor.

Gnometab's features include copying and pasting of tablature passages, a chord
library (which the user must fill with chords), professional-looking rhythm
notation (not perfect yet), the ability to create a variety of tablature symbols
specific to the guitar -- bends, slurs (hammer-ons, pull-offs, etc.), etc. --
and, of course, clean-looking printed output, given any postscript-compatible
printer.

Gnometab does not attempt to be "smart", i.e., it does not know how many
beats are in a measure, nor does it know an E chord from an Am chord.
Instead, the emphasis has been on the appearance of the output.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall

%{__install} -Dp -m0644 gnometab.1 %{buildroot}%{_mandir}/man1/gnometab.1

%if %{dfi}
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor gnome --delete-original \
                --add-category X-Red-Hat-Base                 \
                --add-category Application                    \
                --add-category Utility                        \
                --dir %{buildroot}%{_datadir}/applications    \
                %{buildroot}%{_datadir}/gnome/apps/Applications/%{name}.desktop
%endif

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/*
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/pixmaps/gnometab/
%if %{dfi}
        %{_datadir}/gnome/apps/Applications/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.4-0.2
- Rebuild for Fedora Core 5.

* Mon Apr 28 2003 Dag Wieers <dag@wieers.com> - 0.7.4-0
- Initial package. (using DAR)
