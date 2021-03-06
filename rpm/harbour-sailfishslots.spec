# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-sailfishslots

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libapplicationsettings|libcore|liblanguage.*$
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    SailfishSlots
Version:    1.0
Release:    0
Group:      Qt/Qt
License:    GPLv3
URL:        https://github.com/prplmnky/harbour-sailfishslots
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Slot Machine


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%attr(755, root, root) %{_bindir}/%{name}
%attr(755, root, root) %{_datadir}/%{name}
%attr(644, root, root) %{_datadir}/%{name}/qml/*.qml
%attr(644, root, root) %{_datadir}/%{name}/qml/cover/*.qml
%attr(644, root, root) %{_datadir}/%{name}/qml/pages/*.qml
%attr(644, root, root) %{_datadir}/%{name}/translations/*.qm
%attr(644, root, root) %{_datadir}/%{name}/sounds/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/QmlLogger/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishSlots/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/Components/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/Database/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/FileManagement/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/JS/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/Language/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/Settings/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/Utilities/*
%attr(644, root, root) %{_datadir}/%{name}/harbour/sailfishslots/SailfishWidgets/*.qmltypes
%attr(644, root, root) %{_datadir}/applications/%{name}.desktop
%attr(644, root, root) %{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%attr(644, root, root) %{_datadir}/icons/hicolor/108x108/apps/%{name}.png
%attr(644, root, root) %{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%attr(644, root, root) %{_datadir}/icons/hicolor/172x172/apps/%{name}.png
# >> files
# << files
